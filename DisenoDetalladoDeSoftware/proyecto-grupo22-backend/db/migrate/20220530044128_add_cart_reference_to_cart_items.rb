class AddCartReferenceToCartItems < ActiveRecord::Migration[7.0]
  def change
    add_column :cart_items, :shopping_cart_id, :integer
    add_index :cart_items, :shopping_cart_id

  end
end
