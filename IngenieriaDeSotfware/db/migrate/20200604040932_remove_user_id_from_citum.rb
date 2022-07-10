class RemoveUserIdFromCitum < ActiveRecord::Migration[5.2]
  def change
    remove_column :cita, :user_id, :int
  end
end
