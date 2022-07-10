class AddIsPendingToRestaurants < ActiveRecord::Migration[5.2]
  def change
    add_column :restaurants, :is_pending, :boolean
  end
end
