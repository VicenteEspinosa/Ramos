class CitiesController < ApplicationController
  def index
    @cities = City.all
  end

  def show
    @city = City.find(params[:id])
  end

  def new
    @city = City.new
  end

  def create
    cities_params = params.require(:city).permit(:name)
    @city = City.create(cities_params)

    if @city.save
      redirect_to cities_new_path, notice: 'Ciudad Creada Exitosamente'
    else
      redirect_to cities_new_path, notice: 'Hubo Algun Error Al Crear La Ciudad'
    end
  end

  def edit
    @city = City.find(params[:id])
  end

  def update
    city_params = params.require(:city).permit(:name)
    @city = City.find(params[:id])
    if @city.update(city_params)
      redirect_to city_path(@city.id), notice: 'Ciudad editada correctamente'
    else
      redirect_to city_path(@city.id), notice: 'Ocurrio un error al editar la ciudad'
    end
  end

  def destroy
    @city = City.find(params[:id])
    @city.destroy
    redirect_to cities_path, notice: 'Ciudad eliminada'
  end
end
