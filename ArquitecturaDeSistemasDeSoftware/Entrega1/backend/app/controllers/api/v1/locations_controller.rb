class Api::V1::LocationsController < ApplicationController
  before_action :set_location, only: %i[ show update destroy ]

  # GET /locations
  def index
    @locations = Location.all

    render json: @locations
  end

  # GET /locations/1
  def show
    render json: @location
  end

  # POST /locations
  def create
    @location = Location.new(location_params)



    if @location.save
      render json: @location, status: :created, location: @location
    else
      render json: @location.errors, status: :unprocessable_entity
    end
  end

  def user_locations
    @user = User.find(params[:user_id])
    @locations = @user.location
    render json: @locations
  end

  def multiple_user_locations
    response = {}
    params[:users_ids].split(',').first(5).each do |user_id|
      next unless User.exists?(user_id)
      user = User.find(user_id)
      response[user.id] = {
        locations: Location.where(user_id: user.id).map { |location| LocationSerializer.new(location)},
        username: user.username
      }
    end
    render json: response
  end

  # DELETE /locations/1
  def destroy
    @location.destroy
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_location
      @location = Location.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def location_params
      params.require(:location).permit(:lat, :long, :name, :user_id, :users_ids)
    end
end
