import React, { useState, useMemo } from "react";
import "./FormPanel.css";

export default function FormPanel({ closeForm, days, timeSlots, schedules, addSchedule }) {
  const [subject, setSubject] = useState("");
  const [teacher, setTeacher] = useState("");
  const [section, setSection] = useState("");
  const [day, setDay] = useState(days[0]);
  const [shift, setShift] = useState("morning");
  const [timeIn, setTimeIn] = useState("");
  const [timeOut, setTimeOut] = useState("");

  const filteredTimes = useMemo(() => {
    let start, end;
    if (shift === "morning") [start, end] = ["07:00", "11:00"];
    if (shift === "afternoon") [start, end] = ["11:30", "15:30"];
    if (shift === "evening") [start, end] = ["16:00", "20:30"];
    const startIndex = timeSlots.indexOf(start);
    const endIndex = timeSlots.indexOf(end);
    return timeSlots.slice(startIndex, endIndex + 1);
  }, [shift, timeSlots]);

  const isTimeDisabled = (slot) => schedules[`${day}-${slot}`] !== undefined;

  const handleSubmit = (e) => {
    e.preventDefault();
    addSchedule({ subject, teacher, section, day, timeIn, timeOut });
  };

  return (
    <div className="form-panel">
      <h2 className="form-title">Add Schedule</h2>
      <form onSubmit={handleSubmit} className="form">
        <input
          type="text"
          placeholder="Subject Code"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Subject Name / Section"
          value={section}
          onChange={(e) => setSection(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Professor Name"
          value={teacher}
          onChange={(e) => setTeacher(e.target.value)}
          required
        />

        <div>
          <label>Day</label>
          <select value={day} onChange={(e) => setDay(e.target.value)}>
            {days.map((d) => (
              <option key={d} value={d}>{d}</option>
            ))}
          </select>
        </div>

        <div>
          <label>Shift</label>
          <div className="radio-group">
            {["morning", "afternoon", "evening"].map((s) => (
              <label key={s}>
                <input
                  type="radio"
                  name="shift"
                  value={s}
                  checked={shift === s}
                  onChange={(e) => setShift(e.target.value)}
                />
                {s.charAt(0).toUpperCase() + s.slice(1)}
              </label>
            ))}
          </div>
        </div>

        <div>
          <label>Time In</label>
          <select value={timeIn} onChange={(e) => setTimeIn(e.target.value)}>
            <option value="">Select</option>
            {filteredTimes.map((t) => (
              <option key={t} value={t} disabled={isTimeDisabled(t)}>
                {t}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label>Time Out</label>
          <select value={timeOut} onChange={(e) => setTimeOut(e.target.value)}>
            <option value="">Select</option>
            {filteredTimes.map((t) => (
              <option
                key={t}
                value={t}
                disabled={isTimeDisabled(t) || (timeIn && t <= timeIn)}
              >
                {t}
              </option>
            ))}
          </select>
        </div>

        <div className="form-actions">
          <button type="submit" className="save-btn">Save</button>
          <button type="button" onClick={closeForm} className="cancel-btn">Cancel</button>
        </div>
      </form>
    </div>
  );
}
