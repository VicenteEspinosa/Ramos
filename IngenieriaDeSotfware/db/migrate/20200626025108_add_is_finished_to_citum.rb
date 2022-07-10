class AddIsFinishedToCitum < ActiveRecord::Migration[5.2]
  def change
    add_column :cita, :is_finished, :boolean, :default => false
  end
end
