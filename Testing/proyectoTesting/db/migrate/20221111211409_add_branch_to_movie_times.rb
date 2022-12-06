class AddBranchToMovieTimes < ActiveRecord::Migration[7.0]
  def change
    add_column :movie_times, :branch, :string, default: 'Santiago'
  end
end
