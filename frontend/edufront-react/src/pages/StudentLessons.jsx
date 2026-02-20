// src/pages/StudentLessons.jsx
import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/useAuth';
import api from '../api';
import { useNavigate } from 'react-router-dom';

const StudentLessons = () => {
  const { user } = useAuth();
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const FIXED_SUBJECT = 'Алгоритмизация и программирование';

  const navigate = useNavigate();

  useEffect(() => {
    const fetchLessons = async () => {
      try {
        const response = await api.get('/lessons-detailed');
        const filtered = response.data.filter(
          lesson => lesson.group_name === user.groupName && lesson.subject_name === FIXED_SUBJECT
        );
        setLessons(filtered);
      } catch (error) {
        console.error('Ошибка загрузки занятий:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchLessons();
  }, [user.groupName]);

  const formatDate = (dateStr) => {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    return d.toLocaleDateString('ru-RU', { day: 'numeric', month: 'numeric', year: 'numeric' });
  };

  const handleUpload = () => alert('Загрузка задания будет позже');
  // const handleCheck = () => alert('Проверка решения будет позже');
  const handleCheck = (lessonId) => { navigate(`/student/check/${lessonId}`); };

  if (loading) return <div className="loading">Загрузка заданий...</div>;

  return (
    <div className="student-lessons">
      <h2>Мои задания</h2>
      {lessons.length === 0 ? (
        <p className="empty-state">Нет доступных заданий</p>
      ) : (
        lessons.map(lesson => (
          <div key={lesson.lesson_id} className="lesson-card">
            <div className="card-header">
              <span className="card-date">{formatDate(lesson.lesson_date)}</span>
              <span className="card-subject">{lesson.subject_name}</span>
            </div>
            <div className="lesson-group">
              <span className="section-title">Группа:</span> {lesson.group_name}
            </div>
            <div className="lesson-description">
              <span className="section-title">Описание:</span><br/>
              {lesson.assignment_description || 'Нет описания'}
            </div>
            <div className="lesson-task">
              <span className="section-title">Задание:</span>
              {lesson.attachment_path ? (
                <a href={lesson.attachment_path} target="_blank" rel="noopener noreferrer" className="task-link">
                  📎 {lesson.assignment_number}.pdf
                </a>
              ) : (
                <span className="no-file">Нет файла</span>
              )}
            </div>
            <div className="lesson-actions">
              <button className="button-small upload-btn" onClick={handleUpload}>
                Загрузить задание
              </button>
              <button className="button-small check-btn"  onClick={() => handleCheck(lesson.lesson_id)}>
                Проверить решение
              </button>
            </div>
            <div className="lesson-materials">
              <span className="section-title">Материалы (обучающие ресурсы):</span>
              <span className="no-info">Нет информации</span>
            </div>
          </div>
        ))
      )}
    </div>
  );
};

export default StudentLessons;

// =========================================================
// 1-я версия - один файл StudentLessons.jsx без шапки с приветствием, без меню
// import React, { useState, useEffect } from 'react';
// import { useAuth } from '../context/useAuth';
// import api from '../api';

// const StudentLessons = () => {
//   const { user } = useAuth();
//   const [lessons, setLessons] = useState([]);
//   const [loading, setLoading] = useState(true);
//   const FIXED_SUBJECT = 'Алгоритмизация и программирование';

//   useEffect(() => {
//     const fetchLessons = async () => {
//       try {
//         const response = await api.get('/lessons-detailed');
//         // Фильтруем по группе студента и фиксированному предмету
//         const filtered = response.data.filter(
//           lesson => lesson.group_name === user.groupName && lesson.subject_name === FIXED_SUBJECT
//         );
//         setLessons(filtered);
//       } catch (error) {
//         console.error('Ошибка загрузки занятий:', error);
//       } finally {
//         setLoading(false);
//       }
//     };
//     fetchLessons();
//   }, [user.groupName]);

//   const formatDate = (dateStr) => {
//     if (!dateStr) return '';
//     const d = new Date(dateStr);
//     return d.toLocaleDateString('ru-RU', { day: 'numeric', month: 'numeric', year: 'numeric' });
//   };

//   const handleUpload = () => {
//     alert('Функция загрузки задания будет реализована позже');
//   };

//   const handleCheck = () => {
//     alert('Функция проверки решения будет реализована позже');
//   };

//   if (loading) return <div className="loading">Загрузка заданий...</div>;

//   return (
//     <div className="student-lessons">
//       <h2>Мои задания</h2>
//       {lessons.length === 0 ? (
//         <p className="empty-state">Нет доступных заданий</p>
//       ) : (
//         lessons.map(lesson => (
//           <div key={lesson.lesson_id} className="lesson-card">
//             {/* Верхняя строка: дата и дисциплина */}
//             <div className="card-header">
//               <span className="card-date">{formatDate(lesson.lesson_date)}</span>
//               <span className="card-subject">{lesson.subject_name}</span>
//             </div>

//             {/* Группа */}
//             <div className="lesson-group">
//               <span className="section-title">Группа:</span> {lesson.group_name}
//             </div>

//             {/* Описание */}
//             <div className="lesson-description">
//               <span className="section-title">Описание:</span>
//               <p>{lesson.assignment_description || 'Нет описания'}</p>
//             </div>

//             {/* Задание (файл) */}
//             <div className="lesson-task">
//               <span className="section-title">Задание:</span>
//               {lesson.attachment_path ? (
//                 <a href={lesson.attachment_path} target="_blank" rel="noopener noreferrer" className="task-link">
//                   📎 {lesson.assignment_number}.pdf
//                 </a>
//               ) : (
//                 <span className="no-file">Нет файла</span>
//               )}
//             </div>

//             {/* Кнопки */}
//             <div className="lesson-actions">
//               <button className="button-small upload-btn" onClick={handleUpload}>
//                 Загрузить задание
//               </button>
//               <button className="button-small check-btn" onClick={handleCheck}>
//                 Проверить решение
//               </button>
//             </div>

//             {/* Материалы (заглушка) */}
//             <div className="lesson-materials">
//               <span className="section-title">Материалы (обучающие ресурсы):</span>
//               <span className="no-info">Нет информации</span>
//             </div>
//           </div>
//         ))
//       )}
//     </div>
//   );
// };

// export default StudentLessons;