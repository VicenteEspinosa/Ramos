class CategoriesController < ApplicationController

  def index
    render json: {data: Category.all}, status: 200
  end

  def create
    @category = Category.create(category_params)

    if @category.save
      render json: {data: "Categoría agregada correctamente"}, status: 201
    else
      render json: {data: "No se pudo agregar la categoría..."}, status: 400
    end
  end

  def update
    @category = Category.find(params[:id])
  end

  def destroy
    @category = Category.find(params[:id])
    @category.destroy

    render json: {data: "Categoría eliminada correctamente..."}, status: 200
  end

  private

    def category_params
      params.require(:category).permit(:name)
    end
end
