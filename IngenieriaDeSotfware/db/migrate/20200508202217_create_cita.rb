class CreateCita < ActiveRecord::Migration[5.2]
  def change
    create_table :cita do |t|
      t.integer :user_id
      t.integer :restaurant_id
      t.date :date

      t.timestamps
    end
  end
end
