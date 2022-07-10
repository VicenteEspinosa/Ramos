class CitaController < ApplicationController
  before_action :set_citum, only: [:show, :edit, :update, :destroy]

  # GET /cita
  # GET /cita.json
  def index
    @cita = Citum.all
  end

  # GET /cita/1
  # GET /cita/1.json
  def show
    if user_signed_in?
      @date = Citum.find(params[:id])
      @restaurant = Restaurant.find(@date.restaurant_id)
      if @date.user_id == current_user.id
        @dated_user = User.find(@date.user_2_id)
      elsif @date.user_2_id == current_user.id
        @dated_user = User.find(@date.user_id)
      end
    else
      redirect_to new_user_registration_path
    end
  end

  # GET /cita/new

  def new
    @user_2_id = params[:user_2_id]
    @citum = Citum.new
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

  # GET /cita/1/edit
  def edit
  end

  # POST /cita
  # POST /cita.json
  def create
    @citum = Citum.new(citum_params)
    respond_to do |format|
      if @citum.save
        format.html { redirect_to show_user_matches_path, notice: 'Citum was successfully created.' }
        format.json { render :show, status: :created, location: @citum }
      else
        format.html { redirect_to show_user_matches_path, notice: 'Error.' }
        format.json { render json: @citum.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /cita/1
  # PATCH/PUT /cita/1.json
  def update
    respond_to do |format|
      if @citum.update(citum_params)
        format.html { redirect_to @citum, notice: 'Citum was successfully updated.' }
        format.json { render :show, status: :ok, location: @citum }
      else
        format.html { render :edit }
        format.json { render json: @citum.errors, status: :unprocessable_entity }
      end
    end
  end

  def check_citum
    citum_params = params.permit(:is_checked, :is_finished, :citum_id)
    @citum = Citum.find(citum_params[:citum_id])
    @citum.update_attribute(:is_checked, citum_params[:is_checked])
    @citum.update_attribute(:is_finished, citum_params[:is_finished])
    redirect_to show_user_dates_path
  end

  # DELETE /cita/1
  # DELETE /cita/1.json
  def destroy
    @citum.destroy
    respond_to do |format|
      format.html { redirect_to cita_url, notice: 'Citum was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_citum
    @citum = Citum.find(params[:id])
  end

  # Only allow a list of trusted parameters through.
  def citum_params
    params.require(:citum).permit(:user_id, :restaurant_id, :date, :user_2_id)
  end
end
