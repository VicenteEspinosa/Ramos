class AddLanguageToMovieTimes < ActiveRecord::Migration[7.0]
  def change
    add_column :movie_times, :language, :string, default: 'Ingles'
  end
end
