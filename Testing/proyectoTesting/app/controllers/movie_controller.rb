# frozen_string_literal: true

# Controler that manages all actions related to movie creation, room assignment and movie schedule
class MovieController < ApplicationController
  def home; end

  def new
    @movie_times = MovieTime.new
  end

  def post
    title = params[:title]
    image = params[:image]
    @movie = Movie.new(title:, image:)
    if @movie.save
      redirect_to '/movie/new', notice: 'Pelicula creada con exito'
    else
      redirect_to '/movie/new', notice: @movie.errors.messages
    end
  end

  def create_movie_time
    movie_time_params = params.require(:movie_time).permit(:movie_id, :time, :date_start,
                                                           :date_end, :room, :rating,
                                                           :branch, :language)
    movie_time = MovieTime.create(movie_time_params)
    if movie_time.persisted?
      redirect_to '/movie/new', notice: 'Pelicula asignada con exito'
    else
      redirect_to '/movie/new', notice: movie_time.errors.messages
    end
  end

  def list_by_date
    @date = params[:date]
    @rating = params[:rating]
    @branch = params[:branch]
    @language = params[:language]
    if @rating == 'TODO ESPECTADOR'
      # rubocop:disable Layout/LineLength
      initial_filter = Movie.includes(:movie_times).where(['movie_times.date_start <= ? and ? <= movie_times.date_end and movie_times.branch = ? and movie_times.rating = ?', @date, @date, @branch, @rating]).references(:movie_times)
    else
      initial_filter = Movie.includes(:movie_times).where(['movie_times.date_start <= ? and ? <= movie_times.date_end and movie_times.branch = ?', @date, @date, @branch]).references(:movie_times)
      # rubocop:enable Layout/LineLength
    end
    @filter = if @language == 'Ingles'
                initial_filter.in_order_of(:language, %w[Ingles Español])
              else
                initial_filter.in_order_of(:language, %w[Español Ingles])
              end
  end
end
