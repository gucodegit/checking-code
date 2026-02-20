// pages/LessonList.jsx
import React, { useState, useEffect } from 'react';
import api from '../api';

// Функции определены вне компонента — они не будут пересоздаваться при рендерах
async function loadGroups(setGroups) {
  try {
    const response = await api.get('/groups');
    setGroups(response.data);
  } catch (error) {
    console.error('Ошибка загрузки групп:', error);
  }
}

async function loadLessons(setAllLessons) {
  try {
    const response = await api.get('/lessons-detailed');
    setAllLessons(response.data);
  } catch (error) {
    console.error('Ошибка загрузки занятий:', error);
  }
}

const LessonList = () => {
  const [groups, setGroups] = useState([]);
  const [allLessons, setAllLessons] = useState([]);
  const [filteredLessons, setFilteredLessons] = useState([]);
  const [selectedGroupId, setSelectedGroupId] = useState('');
  const [selectedGroupName, setSelectedGroupName] = useState('');
  const FIXED_SUBJECT = 'Алгоритмизация и программирование';

  useEffect(() => {
    loadGroups(setGroups);
    loadLessons(setAllLessons);
  }, []); // зависимости пустые — выполнится один раз

  const handleGroupChange = (e) => {
    const groupId = parseInt(e.target.value);
    setSelectedGroupId(groupId);
    const groupName = e.target.selectedOptions[0]?.text || '';
    setSelectedGroupName(groupName);
    filterLessons(groupName);
  };

  const filterLessons = (groupName) => {
    if (!groupName) {
      setFilteredLessons([]);
      return;
    }
    const filtered = allLessons.filter(lesson =>
      lesson.group_name === groupName && lesson.subject_name === FIXED_SUBJECT
    );
    setFilteredLessons(filtered);
  };

  const formatDate = (dateStr) => {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    return d.toLocaleDateString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' });
  };

  const renderTable = () => {
    if (filteredLessons.length === 0) {
      return <div className="empty-state"><p>Нет занятий для выбранной группы</p></div>;
    }

    return (
      <table className="lessons-table" id="lessonsTable">
        <thead>
          <tr>
            <th>Дата занятия</th>
            <th>Номер задания</th>
            <th>Описание задания</th>
            <th>Срок выполнения</th>
            <th>Материалы</th>
          </tr>
        </thead>
        <tbody>
          {filteredLessons.map(lesson => (
            <tr key={lesson.lesson_id}>
              <td><strong>{formatDate(lesson.lesson_date)}</strong></td>
              <td><strong>{lesson.assignment_number}</strong></td>
              <td className="assignment-description">{lesson.assignment_description || <span style={{ color: '#666', fontStyle: 'italic' }}>Описание отсутствует</span>}</td>
              <td>
                {lesson.assignment_deadline ? (
                  <span className={new Date(lesson.assignment_deadline) < new Date() ? 'deadline-warning' : 'deadline-normal'}>
                    {formatDate(lesson.assignment_deadline)}
                  </span>
                ) : <span style={{ color: '#666' }}>Не указан</span>}
              </td>
              <td>
                {lesson.attachment_path ? (
                  <a href={lesson.attachment_path} className="attachment-link" target="_blank" rel="noopener noreferrer">📎 Скачать</a>
                ) : <span style={{ color: '#666' }}>—</span>}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  };

  return (
    <div className="form-container">
      <h2>Список занятий</h2>
      <h3>Дисциплина: {FIXED_SUBJECT}</h3>
      <div className="stats" id="statsInfo">
        {selectedGroupId ? (
          <strong>Группа: {selectedGroupName} | Всего занятий: {filteredLessons.length}</strong>
        ) : <strong>Статистика:</strong>}
      </div>
      <div className="filters">
        <div className="form-group">
          <label>Выберите группу:</label>
          <select id="groupFilter" required value={selectedGroupId} onChange={handleGroupChange}>
            <option value="">Выберите группу...</option>
            {groups.map(group => <option key={group.group_id} value={group.group_id}>{group.group_name}</option>)}
          </select>
        </div>
      </div>
      {renderTable()}
    </div>
  );
};

export default LessonList;
