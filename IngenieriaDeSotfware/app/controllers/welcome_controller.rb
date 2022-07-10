class WelcomeController < ApplicationController
  def home
    @matches = Match.where(is_match: true)
    @quantity = 0
    @matches.each do |match|
      half_match = Match.where(user_id: match.user_2_id, user_2_id: match.user_id, is_match: true)
      if !half_match.empty?
        @quantity += 1
      end
    end
    @quantity /= 2
    @approved_restaurants = Restaurant.where(is_approved: true)
  end
end
