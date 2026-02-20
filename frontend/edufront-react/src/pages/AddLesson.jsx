import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import api from '../api';

const AddLesson = () => {
//   const navigate = useNavigate();
  const [formData, setFormData] = useState({
    lesson_date: '',
    lesson_time: '',
    assignment_number: '',
    assignment_description: '',
    attachment_path: '',
    assignment_deadline: '',
    group_id: '',
    subject_id: ''
  });
  const [message, setMessage] = useState({ text: '', type: '' });

  // Запрос групп
  const { data: groups = [], isLoading: groupsLoading } = useQuery({
    queryKey: ['groups'],
    queryFn: async () => {
      const response = await api.get('/groups');
      return response.data;
    },
  });

  // Запрос предметов
  const { data: subjects = [], isLoading: subjectsLoading } = useQuery({
    queryKey: ['subjects'],
    queryFn: async () => {
      const response = await api.get('/subjects');
      return response.data;
    },
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.id]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const payload = {
        ...formData,
        group_id: parseInt(formData.group_id),
        subject_id: parseInt(formData.subject_id),
        assignment_description: formData.assignment_description || null,
        attachment_path: formData.attachment_path || null,
        assignment_deadline: formData.assignment_deadline || null
      };
      const response = await api.post('/lessons', payload);
      setMessage({ text: `Занятие успешно добавлено! ID: ${response.data.lesson_id}`, type: 'success' });
      setFormData({
        lesson_date: '',
        lesson_time: '',
        assignment_number: '',
        assignment_description: '',
        attachment_path: '',
        assignment_deadline: '',
        group_id: '',
        subject_id: ''
      });
    } catch (error) {
      setMessage({ text: `Ошибка: ${error.response?.data?.detail || error.message}`, type: 'error' });
    }
  };

  if (groupsLoading || subjectsLoading) {
    return <div className="loading">Загрузка данных...</div>;
  }

  return (
    <div className="lesson-card add-lesson-card">
      <h2 className="card-title">Добавить новое занятие</h2>
      <form onSubmit={handleSubmit} className="add-lesson-form">

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="group_id">Группа</label>
            <select id="group_id" required value={formData.group_id} onChange={handleChange}>
              <option value="">Выберите группу</option>
              {groups.map(g => <option key={g.group_id} value={g.group_id}>{g.group_name}</option>)}
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="subject_id">Дисциплина</label>
            <select id="subject_id" required value={formData.subject_id} onChange={handleChange}>
              <option value="">Выберите дисциплину</option>
              {subjects.map(s => <option key={s.subject_id} value={s.subject_id}>{s.subject_name}</option>)}
            </select>
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="assignment_number">Номер задания</label>
            <input type="text" id="assignment_number" required value={formData.assignment_number} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="assignment_deadline">Срок выполнения</label>
            <input type="date" id="assignment_deadline" value={formData.assignment_deadline} onChange={handleChange} />
          </div>
        </div>

        <div className="form-group full-width">
          <label htmlFor="assignment_description">Описание задания</label>
          <textarea id="assignment_description" rows="4" value={formData.assignment_description} onChange={handleChange} />
        </div>

        <div className="form-group full-width">
          <label htmlFor="attachment_path">Путь к вложению</label>
          <input type="text" id="attachment_path" value={formData.attachment_path} onChange={handleChange} />
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="lesson_date">Дата занятия</label>
            <input type="date" id="lesson_date" required value={formData.lesson_date} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="lesson_time">Время занятия</label>
            <input type="time" id="lesson_time" required value={formData.lesson_time} onChange={handleChange} />
          </div>
        </div>

        <div className="form-actions">
          <button type="submit" className="submit-btn">Добавить занятие</button>
        </div>
      </form>
      {message.text && <div className={`message ${message.type}`}>{message.text}</div>}
    </div>
  );
};

export default AddLesson;