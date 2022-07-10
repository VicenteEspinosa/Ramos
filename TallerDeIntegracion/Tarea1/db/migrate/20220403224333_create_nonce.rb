class CreateNonce < ActiveRecord::Migration[7.0]
  def change
    create_table :nonces do |t|
      t.string :value
      t.integer :expiration

      t.timestamps
    end
  end
end
