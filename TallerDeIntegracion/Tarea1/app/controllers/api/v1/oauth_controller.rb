class Api::V1::OauthController < ApplicationController
  before_action :validate_scope, :validate_user

  def request_token
    nonce = 1.times.map { (0...((20))).map { ('a'..'z').to_a[rand(26)] }.join }.join(" ")
    expiration = (Time.now).to_time.to_i + 10
    nonce_model = Nonce.new(value: nonce, expiration: expiration, user_id: request.query_parameters[:user_id], scopes: [request.query_parameters[:scopes]])
    nonce_model.save
    return render json: {
      message: "#{request.query_parameters[:app_id]} está intentado acceder a #{request.query_parameters[:scopes]}, ¿desea continuar?",
      grant_url: "/oauth/grant?user_id=#{request.query_parameters[:user_id]}&scopes=#{request.query_parameters[:scopes]}&app_id=#{request.query_parameters[:app_id]}&nonce=#{nonce}",
      expiration: expiration
    }.as_json, status: 200
  end

  private

  def scopes
    ['basic', 'education', 'work', 'medical']
  end

  def validate_scope
    request.query_parameters[:scopes].split(',').each do |scope|
      unless scopes.include?(scope)
        return render json: {error: 'invalid scope'}.as_json, status: 400
      end
    end
    params_oauth.each do |param|
      if request.query_parameters[param].nil? || request.query_parameters[param].empty?
        request.query_parameters[param]
        return render json: {error: "invalid oauth grant"}.as_json, status: 400
      end
    end
  end

  def validate_user
    user = User.find_by(id: request.query_parameters[:user_id])
    if user.nil?
      return render json: {error: 'invalid user'}.as_json, status: 404
    end
  end

  def params_oauth
    ['user_id', 'scopes', 'app_id']
  end
end
