class AddActiveToShoppingCart < ActiveRecord::Migration[7.0]
  def change
    add_column :shopping_carts, :active, :boolean, default: true
  end
end
