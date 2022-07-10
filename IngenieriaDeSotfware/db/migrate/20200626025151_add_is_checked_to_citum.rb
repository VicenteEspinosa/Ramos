class AddIsCheckedToCitum < ActiveRecord::Migration[5.2]
  def change
    add_column :cita, :is_checked, :boolean, :default => false
  end
end
