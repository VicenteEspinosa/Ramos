class CommentsController < ApplicationController
  def index
    @comments = Comment.all
  end

  def show
    @comment = Comment.find(params[:id])
  end

  def new
    @comment = Comment.new
  end

  def create
    comment_params = params.require(:comment).permit(:content, :rating, :user_id, :restaurant_id)
    @comment = Comment.create(comment_params)
    if @comment.save
      redirect_to restaurant_path(comment_params[:restaurant_id]), notice: 'Comentario creado exitosamente'
    else
      redirect_to comments_new_path, notice: 'Hubo un error al crear el comentario'
    end
  end

  def edit
    @comment = Comment.find(params[:id])
  end

  def update
    comment_params = params.require(:comment).permit(:content, :rating)
    @comment = Comment.find(params[:id])
    if @comment.update(comment_params)
      redirect_to comment_edit_path(@comment.id), notice: 'Comentario editado con éxito'
    else
      redirect_to comment_edit_path(@comment.id), notice: 'Ocurrió un error al editar el comentario'
    end
  end

  def destroy
    @comment = Comment.find(params[:id])
    @comment.destroy
    redirect_to restaurant_path(params[:restaurant_id])
  end
end
