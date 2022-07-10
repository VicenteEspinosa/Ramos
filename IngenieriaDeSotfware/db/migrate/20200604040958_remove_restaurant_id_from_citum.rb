class RemoveRestaurantIdFromCitum < ActiveRecord::Migration[5.2]
  def change
    remove_column :cita, :restaurant_id, :int
  end
end
