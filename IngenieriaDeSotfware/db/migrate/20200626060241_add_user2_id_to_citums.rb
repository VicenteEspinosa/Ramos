class AddUser2IdToCitums < ActiveRecord::Migration[5.2]
  def change
    add_column :cita, :user_2_id, :integer
  end
end
