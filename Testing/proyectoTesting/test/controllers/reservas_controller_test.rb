# frozen_string_literal: true

require 'test_helper'

class ReservasControllerTest < ActionDispatch::IntegrationTest
  def setup
    movie = Movie.create(title: 'Matrix')
    MovieTime.create(room: 5, date_start: Date.new(2000, 11, 10),
                     date_end: Date.new(2000, 11, 12), time: 'TANDA',
                     movie_id: movie.id)
  end

  def teardown
    Reserva.destroy_all
    MovieTime.destroy_all
    Movie.destroy_all
  end

  test 'Posting a new reserva' do
    assert_difference 'Reserva.count' do
      post new_reserva_url(5, '2000-11-12', 'TANDA'),
           params: { reservation_seats: 'C-3', name: 'Diego' }
    end
  end

  test 'POST reserva valid' do
    post '/reservas/new/5/2022-10-11/TANDA', params:
      {
        reservation_seats: 10,
        name: 'Pedro'
      }
    assert_response :redirect
  end

  test 'POST reserva without name' do
    post '/reservas/new/5/2022-10-11/TANDA', params: { reservation_seats: 10 }
    assert_response :redirect
  end

  test 'POST reserva with invalid seat' do
    post '/reservas/new/5/2022-10-11/TANDA', params: { reservation_seats: 200, name: 'Pedro' }
    assert_response :redirect
  end

  test 'POST reserva no selected seat' do
    post '/reservas/new/5/2022-10-11/TANDA', params: { reservation_seats: '', name: 'Pedro' }
    assert_response :redirect
  end

  test 'GET reserva' do
    Reserva.create(sala: 5, fecha: Date.new(2022, 10, 11), asiento: 10, horario: 'TANDA',
                   name: 'Pedro')
    get '/reservas/new/5/2022-10-11/TANDA'
    assert_response :success
  end
end
