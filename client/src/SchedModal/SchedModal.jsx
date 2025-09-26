import React, { useState } from "react";
import FormPanel from "../FormModal/FormPanel";
import "./SchedModal.css";

export default function SchedModal({ closeModal }) {
  const days = ["MON", "TUE", "WED", "THU", "FRI", "SAT"];

  const timeSlots = [];
  for (let hour = 7; hour <= 20; hour++) {
    timeSlots.push(`${hour.toString().padStart(2, "0")}:00`);
    if (hour < 20) timeSlots.push(`${hour.toString().padStart(2, "0")}:30`);
  }

  const [schedules, setSchedules] = useState({});
  const [showForm, setShowForm] = useState(false);

  const addSchedule = (newSched) => {
    setSchedules((prev) => {
      const updated = { ...prev };
      const startIndex = timeSlots.indexOf(newSched.timeIn);
      const endIndex = timeSlots.indexOf(newSched.timeOut);

      for (let i = startIndex; i < endIndex; i++) {
        updated[`${newSched.day}-${timeSlots[i]}`] = {
          subject: newSched.subject,
          teacher: newSched.teacher,
          section: newSched.section,
          timeIn: newSched.timeIn,
          timeOut: newSched.timeOut,
          startIndex,
          endIndex,
          day: newSched.day,            // <-- IMPORTANT: store day
        };
      }
      return updated;
    });

    setShowForm(false);
  };

  // Remove an entire schedule block (uses stored day/startIndex/endIndex)
  const removeSchedule = (cell) => {
    if (!cell || cell.startIndex == null || cell.endIndex == null || !cell.day) {
      console.warn("Unable to remove schedule - invalid cell:", cell);
      return;
    }

    setSchedules((prev) => {
      const updated = { ...prev };
      for (let i = cell.startIndex; i < cell.endIndex; i++) {
        delete updated[`${cell.day}-${timeSlots[i]}`];
      }
      return updated;
    });
  };

  return (
    <div className="sched-overlay" onClick={closeModal}>
      <div
        className={`sched-wrapper ${showForm ? "with-form" : ""}`}
        onClick={(e) => e.stopPropagation()}
      >
        <div className="sched-left">
          <div className="sched-header">
            <h2 className="sched-title">Class Schedule</h2>
            <button onClick={() => setShowForm(true)} className="add-btn">
              Add Schedule
            </button>
          </div>

          <div className="table-container">
            <table className="sched-table">
              <thead>
                <tr>
                  <th>TIME</th>
                  {days.map((day) => (
                    <th key={day}>{day}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {timeSlots.map((time, index) => (
                  <tr key={time}>
                    <td>{time}</td>
                    {days.map((day) => {
                      const cell = schedules[`${day}-${time}`];
                      if (cell && cell.startIndex === index) {
                        return (
                          <td
                            key={day}
                            className="sched-cell-filled"
                            rowSpan={cell.endIndex - cell.startIndex}
                          >
                            <div className="subject">{cell.subject}</div>
                            <div className="subname">{cell.section}</div>
                            <div className="teacher">{cell.teacher}</div>
                            <div className="time">
                              {cell.timeIn} - {cell.timeOut}
                            </div>

                            <button
                              className="remove-btn"
                              onClick={(e) => {
                                e.stopPropagation();     // avoid bubbling issues
                                removeSchedule(cell);
                              }}
                            >
                              Remove
                            </button>
                          </td>
                        );
                      }
                      if (cell && cell.startIndex < index) return null;
                      return <td key={day}></td>;
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        <div className={`sched-right ${showForm ? "open" : ""}`}>
          {showForm && (
            <FormPanel
              closeForm={() => setShowForm(false)}
              days={days}
              timeSlots={timeSlots}
              schedules={schedules}
              addSchedule={addSchedule}
            />
          )}
        </div>
      </div>
    </div>
  );
}
