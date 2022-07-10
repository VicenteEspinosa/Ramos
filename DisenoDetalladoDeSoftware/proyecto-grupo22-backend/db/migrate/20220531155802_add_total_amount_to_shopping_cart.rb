class AddTotalAmountToShoppingCart < ActiveRecord::Migration[7.0]
  def change
    add_column :shopping_carts, :total_amount, :integer, default: 0
  end
end
