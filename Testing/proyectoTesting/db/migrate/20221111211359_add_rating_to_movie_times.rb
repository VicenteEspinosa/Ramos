class AddRatingToMovieTimes < ActiveRecord::Migration[7.0]
  def change
    add_column :movie_times, :rating, :string, default: 'TODO ESPECTADOR'
  end
end
