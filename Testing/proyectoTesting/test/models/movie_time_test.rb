# frozen_string_literal: true

require 'test_helper'

class MovieTimeTest < ActiveSupport::TestCase
  def teardown
    MovieTime.destroy_all
  end

  test 'MovieTime start date is before end date' do
    movie = Movie.create!(title: 'Matrix')
    movie_time = MovieTime.create(
      room: 5,
      date_start: Date.new(2000, 11, 10),
      date_end: Date.new(2000, 11, 9),
      time: 'TANDA',
      movie_id: movie.id
    )
    assert_not movie_time.valid?
  end

  test 'MovieTime in already used time' do
    movie = Movie.create!(title: 'Matrix')
    MovieTime.create!(
      room: 5,
      date_start: Date.new(2000, 12, 1),
      date_end: Date.new(2000, 12, 2),
      time: 'TANDA',
      movie_id: movie.id
    )
    movie_time = MovieTime.new(
      room: 5,
      date_start: Date.new(2000, 12, 1),
      date_end: Date.new(2000, 12, 2),
      time: 'TANDA',
      movie_id: movie.id
    )

    assert_not movie_time.valid?
  end
end
