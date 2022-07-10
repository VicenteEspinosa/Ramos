class MatchesController < ApplicationController
  def index
    @matches = Match.all
  end

  def show
    @match = Match.find(params([:id]))
  end

  def new
    @match = Match.new
  end

  def create
    math_params = params.permit(:user_id, :user_2_id, :is_match)
    @match = Match.create(math_params)
    if @match.save
      redirect_to show_user_recommendations_path, notice: 'Accion realizada con éxito'
    else
      redirect_to show_user_recommendations_path, notice: 'Hubo un error al hacer Match'
    end
  end
end
