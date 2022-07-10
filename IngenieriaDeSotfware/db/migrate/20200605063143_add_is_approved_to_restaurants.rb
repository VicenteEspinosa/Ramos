class AddIsApprovedToRestaurants < ActiveRecord::Migration[5.2]
  def change
    add_column :restaurants, :is_approved, :boolean
  end
end
