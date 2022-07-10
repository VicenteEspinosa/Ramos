class CreatePings < ActiveRecord::Migration[7.0]
  def change
    create_table :pings do |t|
      t.references :sender, null: false
      t.references :receiver, null: false

      t.timestamps
    end
  end
end
