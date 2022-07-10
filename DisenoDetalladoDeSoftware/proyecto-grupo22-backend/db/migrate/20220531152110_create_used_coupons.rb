class CreateUsedCoupons < ActiveRecord::Migration[7.0]
  def change
    create_table :used_coupons do |t|
      t.references :coupon, null: false, foreign_key: true
      t.references :shopping_cart, null: false, foreign_key: true

      t.timestamps
    end
  end
end
