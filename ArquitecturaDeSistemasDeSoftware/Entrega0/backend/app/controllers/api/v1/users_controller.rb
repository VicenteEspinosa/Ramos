class Api::V1::UsersController < ApplicationController
  before_action :set_user, only: %i[ show update destroy ]

  # GET /users
  def index
    @users = User.all

    render json: @users
  end

  # GET /user/1
  def show
    render json: @user
  end

  # POST /users
  def create
    return render json: {error: 'Username taken'}.as_json, status: 401 unless User.find_by(username: params[:username]).nil?
    @user = User.new(user_params)

    if @user.save
      UserMailer.with(user: @user, token: JWT.encode(UserSerializer.new(@user).as_json, ENV['SECRET'])).new_user_email.deliver_now
      render json: @user.as_json, status: :created
    else
      render json: @user.errors, status: :unprocessable_entity
    end
  end

  def login
    @user = User.find_by(username: params[:username])
    return render json: {error: 'Invalid data'}.as_json, status: 400 unless !@user.nil? && @user.password == params[:password]

    token = JWT.encode(UserSerializer.new(@user).as_json, ENV['SECRET'])
    render json: {error: 'Invalid data'}.as_json, status: 400 unless @user
    render json: {token: token}.as_json, status: 201
  end



  private
    # Use callbacks to share common setup or constraints between actions.
    def set_user
      @user = User.find(params[:id])
      render json: {error: 'Invalid data'}.as_json, status: 400 unless @user
    end

    # Only allow a list of trusted parameters through.
    def user_params
      params.require(:user).permit(:username, :mail, :contact, :password)
    end
end
