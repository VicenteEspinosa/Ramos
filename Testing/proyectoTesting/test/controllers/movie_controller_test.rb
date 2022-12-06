# frozen_string_literal: true

require 'test_helper'

class MovieControllerTest < ActionDispatch::IntegrationTest
  def setup; end

  def teardown
    MovieTime.destroy_all
    Movie.destroy_all
  end

  test 'should get new' do
    get movie_new_url
    assert_response :success
  end

  test 'POST movie' do
    post '/movie/new', params: { title: 'Test' }
    assert_equal 'Pelicula creada con exito', flash[:notice]
  end

  test 'POST invalid movie' do
    post '/movie/new', params: { title: nil }
    assert_response :redirect
    assert_equal 'El titulo no puede estar vacio', flash[:notice][:title][0]
  end

  test 'POST correct movie time' do
    movie = Movie.create!(title: 'Test')
    post '/movie_time/new', params:
    {
      movie_time:
      {
        movie_id: movie.id,
        time: 'NOCHE',
        date_start: Date.new(2020, 10, 10),
        date_end: Date.new(2020, 10, 10),
        room: 5
      }
    }
    assert_response :redirect
    assert_redirected_to '/movie/new'
    assert_equal 'Pelicula asignada con exito', flash[:notice]
  end

  test 'POST invalid movie time' do
    movie = Movie.create!(title: 'Test')
    post '/movie_time/new', params:
    {
      movie_time:
      {
        movie_id: movie.id,
        time: nil,
        date_start: Date.new(2020, 10, 10),
        date_end: Date.new(2020, 10, 10),
        room: 5
      }
    }
    assert_response :redirect
    assert_redirected_to '/movie/new'
    assert_equal 'Falta el horario', flash[:notice][:time][0]
  end

  test 'GET movies by date' do
    get '/movies/list', params: { date: Date.new(2020, 10, 10) }
    assert_response :success
  end

  test 'GET movies by date <18 & english' do
    get '/movies/list', params: { date: Date.new(2020, 10, 10), rating: 'TODO ESPECTADOR',
                                  language: 'Ingles' }
    assert_response :success
  end
end
