class UsersController < ApplicationController
  def index
    if user_signed_in? && current_user.admin == true
      @users = User.where.not(id: current_user.id)
    else
      redirect_to home_path
    end
  end

  def show
    @current_user = current_user
  end

  def show_user_gustos
    if user_signed_in?
      @user_gustos = current_user.gustos
    else
      redirect_to new_user_registration_path
    end
  end

  def edit_user_by_admin
    if current_user.admin == true
      @user = User.find(params[:id])
    else
      redirect_to home_path
    end
  end

  def update_user_by_admin
    if current_user.admin == true
      user_params = params.require(:user).permit(:email, :name, :city_id, :birthdate, :description, :phone_number)
      @user = User.find(params[:id])
      if params['borrar_avatar']
        @user.remove_avatar!
        @user.save
      end
      if @user.update(user_params)
        redirect_to index_users_path, notice: 'Usuario editado correctamente'
      else
        redirect_to index_users_path, notice: 'Ocurrio un error al editar el usuario'
      end
    else
      redirect_to home_path
    end
  end

  def show_user_to_admin
    if user_signed_in? && current_user.admin == true
      @user = User.find(params[:id])
    else
      redirect_to home_path
    end
  end

  def show_user_matches
    if user_signed_in?
      @user_matches = Match.select(:user_2_id).where(user_id: current_user.id, is_match: true).map(&:user_2_id)
      @real_matches = []
      @user_matches.each do |user_id|
        matched_user = User.find(user_id)
        matches_matched_user = Match.select(:user_2_id).where(user_id: user_id, is_match: true).map(&:user_2_id)
        if matches_matched_user.include?(current_user.id)
          @real_matches << matched_user
        end
      end
      if !@real_matches.empty?
        @match_has_date = {}
        @real_matches.each do |user|
          citum = Citum.where(user_id: current_user.id, user_2_id: user.id).or(Citum.where(user_id: user.id, user_2_id: current_user.id)).first
          @match_has_date[user.id] = citum
        end
      end
    else
      redirect_to new_user_registration_path
    end
  end

  def show_user_dates
    if user_signed_in?
      @user_dates = Citum.where(user_id: current_user.id).or(Citum.where(user_2_id: current_user.id))
      if !@user_dates.empty?
        @dated_users = {}
        @restaurants = {}
        @user_dates.each do |date|
          if date.user_id == current_user.id
            dated_user = User.find(date.user_2_id)
          elsif date.user_2_id == current_user.id
            dated_user = User.find(date.user_id)
          end
          restaurant = Restaurant.find(date.restaurant_id)
          @dated_users[date.id] = dated_user
          @restaurants[date.id] = restaurant
        end
      end
    else
      redirect_to new_user_registration_path
    end
  end

  def show_user_recommendations
    if user_signed_in?
      @user_matches = Match.select(:user_2_id).where(user_id: current_user.id).map(&:user_2_id)
      @user_matches << current_user.id
      @user_recommendations = User.where.not(id: @user_matches)
    else
      redirect_to new_user_registration_path
    end
  end

  def show_user_postulations
    if user_signed_in?
      @user_postulations = Restaurant.where(user_id: current_user.id)
      if !@user_postulations.empty?
        @postulation_status = {}
        @user_postulations.each do |postulation|
          if postulation.is_pending
            @postulation_status[postulation.id] = 'pendiente'
          else
            if postulation.is_approved
              @postulation_status[postulation.id] = 'aprobada'
            else
              @postulation_status[postulation.id] = 'rechazada'
            end
          end
        end
      end
    else
      redirect_to new_user_registration_path
    end
  end

  def show_user_restaurants
    if user_signed_in?
      @user_restaurants = Restaurant.where(user_id: current_user.id, is_approved: true)
      if !@user_restaurants.empty?
        @restaurant_comments = {}
        @restaurant_ratings = {}
        @restaurant_dates = {}
        @user_restaurants.each do |restaurant|
          @restaurant_comments[restaurant.id] = Comment.where(restaurant_id: restaurant.id)
          if !@restaurant_comments[restaurant.id].empty?
            @restaurant_ratings[restaurant.id] = Comment.where(restaurant_id: restaurant.id).average(:rating).round
          else
            @restaurant_ratings[restaurant.id] = 0
          end
          @restaurant_dates[restaurant.id] = Citum.where(restaurant_id: restaurant.id, is_finished: true)
        end
      end
    else
      redirect_to new_user_registration_path
    end
  end
end
