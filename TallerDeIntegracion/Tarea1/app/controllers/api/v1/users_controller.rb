class Api::V1::UsersController < ApplicationController
  skip_before_action :verify_authenticity_token
  protect_from_forgery with: :null_session
  before_action :validate_query_params, only:[:grant]
  before_action :validate_api_token, except: [:create, :reset]
  before_action :validate_user_token_grant, only: [:grant]
  before_action :validate_nonce, only: [:grant]
  before_action :validate_user_token, except: [:create, :reset, :get_scoped]
  before_action :validate_scope, only: [:get_scoped]
  before_action :permitted_access, except: [:create, :reset, :grant]

  def get
    begin
      user = User.find(params[:id])
    rescue => exception
      return render json: {error: "invalid user id"}.as_json, status: 401
    end

    render json: UserSerializer.new(user).as_json, status: 200
  end

  def grant
    puts "-------"
    puts "GRANT"
    puts "-------"
    return render json: {error: "invalid authorization grant, expired #{Time.now.to_time.to_i - @nonce.expiration.to_i} secs ago"}.as_json, status: 406 unless @nonce.expiration.to_i >= Time.now.to_time.to_i

    return render json: {error: "user not found"}.as_json, status: 404 unless User.exists?(id: request.query_parameters[:user_id])

    payload = UserSerializer.new(User.find_by(id: request.query_parameters['user_id'])).as_json
    payload[:scopes] = [request.query_parameters['scopes'].downcase]
    payload[:secret] = ENV.fetch("PUBLIC_SECRET")
    access_token = JWT.encode(payload, ENV.fetch("SECRET"))
    render json: {access_token: access_token, expiration: (Time.now).to_time.to_i + 60}.as_json, status: 200
    
  end

  def get_scoped
    begin
      user = User.find(params[:id])
    rescue => exception
      return render json: {error: "invalid user id"}.as_json, status: 401
    end
    case params[:scope].downcase
    when 'basic'
      render json: UserBasicSerializer.new(user).as_json, status: 200
    when 'education'
      render json: UserEducationSerializer.new(user).as_json, status: 200
    when 'work'
      render json: UserWorkSerializer.new(user).as_json, status: 200
    when 'medical'
      render json: UserMedicalSerializer.new(user).as_json, status: 200
    else
      render json: {message: "Invalid scope"}.as_json, status: 403
    end
  end

  def reset
    User.destroy_all
    render json: {message: "All users deleted"}.as_json, status: 200
  end

  def create
    if User.exists?(username: params[:username])
      return render json: {message: "Username already exists"}.as_json, status: 409
    end
    params.each do |user_param_key, user_param_value|
      if (is_number?(user_param_value) != params_numerical?[user_param_key.to_sym] && params_numerical?.key?(user_param_key.to_sym)) ||
        (user_param_value.is_a?(String) == params_numerical?[user_param_key.to_sym])
        return render json: {error: 'invalid attributes'}.as_json, status: 400
      end
    end
    begin
      user = User.new(user_params)
      user.save
      payload = UserSerializer.new(user).as_json
      payload[:scopes] = ['user']
      payload[:secret] = ENV.fetch("PUBLIC_SECRET")
      token = JWT.encode(payload, ENV.fetch("SECRET"))
      render json: {id: user.id, token: token}.as_json, status: 201
    rescue => exception
      puts "----- ERROR -----"
      puts exception
      puts "-----------------"
      render json: {error: 'invalid attributes'}.as_json, status: 400
    end
  end

  def patch
    user = User.find_by(id: params[:id])

    if params[:username]
      if User.exists?(username: params[:username])
        return render json: {message: "Username already exists"}.as_json, status: 409 # Conflicto si escribe su usuario y no lo cambia
      end
    end
    user_params.each do |user_param_key, user_param_value|
      next if ['id', 'promotion', 'operations', 'password'].include? user_param_key

      if (params_numerical?.key?(user_param_key.to_sym) && is_number?(user_param_value) != params_numerical?[user_param_key.to_sym]) ||
        (user_param_value.is_a?(String) == params_numerical?[user_param_key.to_sym])
        return render json: {error: 'invalid attributes'}.as_json, status: 400
      end
    end
    if user.update(user_params)
      render json: UserSerializer.new(user).as_json, status: 200
    else
      render json: {error: 'faltan parametros'}.as_json, status: 400
    end
  end

  def delete
    user = User.find_by(id: params[:id])
    user.destroy
    render json: {message: "User deleted"}.as_json, status: 204
  end

  private

  def validate_api_token
    begin
      @decoded ||= JWT.decode(request.authorization, ENV.fetch("SECRET"))[0]
    rescue JWT::DecodeError => exception
      render json: {error: 'Invalid token'}, status: 401
    end
  end

  def validate_user_token
    return render json: {message: "Invalid permission"}.as_json, status: 403 unless @decoded["scopes"] == ['user']
  end

  def user_params
    params.require(:user).permit(
      :username, :password, :name, :age, :psu_score, :university, :gpa_score, :job, :salary,
      :promotion, :hospital, :medical_debt, :operations => []
    )
  end

  def validate_scope
    if @decoded["scopes"].include? params[:scope].downcase && @decoded["scopes"] != ['user']
      render json: {message: "Invalid scope"}.as_json, status: 403
    end
  end

  def permitted_access
    if @decoded["id"].to_i != params[:id].to_i
      render json: {message: "you do not have access to this resource"}.as_json, status: 403
    end
  end

  def is_number?(string)
    true if Float(string) rescue false
  end

  def params_oauth
    ['user_id', 'scopes', 'app_id', 'nonce']
  end

  def params_numerical?
    {
      username: false,
      name: false,
      job: false,
      hospital: false,
      age: true,
      gpa_score: true,
      salary: true,
      psu_score: true,
      medical_debt: true,
      university: false,
    }
  end

  def validate_user_token_grant
    return render json: {message: "Invalid permission, not user token"}.as_json, status: 406 unless @decoded["scopes"] == ['user']
    return render json: {message: "Invalid permission, not your user id"}.as_json, status: 406 unless @decoded["id"].to_i == request.query_parameters["user_id"].to_i
  end

  def validate_query_params
    params_oauth.each do |param|
      if request.query_parameters[param].nil?
        return render json: {error: "invalid oauth grant"}.as_json, status: 400
      end
    end
    return render json: {error: "invalid query param"}.as_json, status: 403 unless is_number?(request.query_parameters["user_id"])
  end

  def validate_nonce
    @nonce = Nonce.find_by(value: request.query_parameters['nonce'])
    return render json: {error: "invalid authorization grant, no valid nonce"}.as_json, status: 406 if @nonce.nil?

    return render json: {error: "invalid oauth grant"}.as_json, status: 403 unless @nonce.user_id.to_i == @decoded["id"].to_i && @nonce.scopes.sort == [request.query_parameters["scopes"]].sort
  end

end
