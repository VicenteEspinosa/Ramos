class RestaurantsController < ApplicationController
  before_action :set_restaurant, only: [:show, :edit, :update, :destroy]

  def index
    @approved_restaurants = Restaurant.where(is_approved: true)
    if !@approved_restaurants.empty?
      @restaurant_comments = {}
      @restaurant_ratings = {}
      @approved_restaurants.each do |restaurant|
        @restaurant_comments[restaurant.id] = Comment.where(restaurant_id: restaurant.id)
        if !@restaurant_comments[restaurant.id].empty?
          @restaurant_ratings[restaurant.id] = Comment.where(restaurant_id: restaurant.id).average(:rating).round
        else
          @restaurant_ratings[restaurant.id] = 0
        end
      end
    end
  end

  def show_postulations
    @pending_restaurants = Restaurant.where(is_pending: true)
  end

  def show
    @comment = Comment.new
    @comments = Comment.where(restaurant_id: params[:id])
    if !@comments.empty?
      @rating = Comment.where(restaurant_id: params[:id]).average(:rating).round
    else
      @rating = 0
    end
  end

  def new
    if user_signed_in?
      @restaurant = Restaurant.new
    else
      redirect_to new_user_registration_path
    end
  end

  def edit
  end

  def create
    @restaurant = Restaurant.new(restaurant_params)

    respond_to do |format|
      if @restaurant.save
        format.html { redirect_to show_user_postulations_path, notice: 'Restaurant was successfully created.' }
        format.json { render :show, status: :created, location: @restaurant }
      else
        format.html { render :new }
        format.json { render json: @restaurant.errors, status: :unprocessable_entity }
      end
    end
  end

  def update
    respond_to do |format|
      if @restaurant.update(restaurant_params)
        format.html { redirect_to restaurants_path, notice: 'Restaurant was successfully updated.' }
        format.json { render :show, status: :ok, location: @restaurant }
      else
        format.html { render :edit }
        format.json { render json: @restaurant.errors, status: :unprocessable_entity }
      end
    end
  end

  def update_postulation
    postulation_params = params.permit(:is_approved, :is_pending, :restaurant_id)
    @restaurant = Restaurant.find(postulation_params[:restaurant_id])
    @restaurant.update_attribute(:is_approved, postulation_params[:is_approved])
    @restaurant.update_attribute(:is_pending, postulation_params[:is_pending])
    redirect_to restaurants_postulations_path
  end

  def destroy
    @restaurant.destroy
    respond_to do |format|
      format.html { redirect_to restaurants_url, notice: 'Restaurant was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private

  def set_restaurant
    @restaurant = Restaurant.find(params[:id])
  end

  def restaurant_params
    params.require(:restaurant).permit(:name, :description, :location, :user_id, :city_id, :is_approved, :is_pending, :avatar)
  end
end
