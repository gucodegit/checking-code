import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../api';

const TeacherLessons = () => {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchLessons();
  }, []);

  const fetchLessons = async () => {
    try {
      const response = await api.get('/lessons-detailed');
      setLessons(response.data);
    } catch (error) {
      console.error('Ошибка загрузки занятий:', error);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateStr) => {
    const d = new Date(dateStr);
    return d.toLocaleDateString('ru-RU', { day: 'numeric', month: 'numeric', year: 'numeric' });
  };

  if (loading) return <div className="loading">Загрузка занятий...</div>;

  return (
    <div className="teacher-lessons">
      {/* Кнопка добавления занятия (можно вынести отдельно, если нужно) */}
      <div className="lessons-header">
        <Link to="/teacher/add-lesson" className="file-select-btn">Добавить занятие</Link>
      </div>

      {lessons.length === 0 ? (
        <p className="empty-state">Нет доступных занятий</p>
      ) : (
        lessons.map(lesson => (
          <div key={lesson.lesson_id} className="lesson-card">
            {/* Верхняя строка: дата и дисциплина (заголовок карточки) */}
            <div className="card-header">
              <span className="card-date">{formatDate(lesson.lesson_date)}</span>
              <span className="card-subject">{lesson.subject_name}</span>
              <div className="card-actions">
                <button className="icon-btn edit-btn" title="Редактировать">✎</button>
                <button className="icon-btn delete-btn" title="Удалить">✖</button>
              </div>
            </div>

            {/* Вторая строка: тип занятия + иконки (если есть) */}
            {/* <div className="card-subheader">
              <span className="lesson-type">Практическое занятие</span> */}
              {/* Здесь можно добавить дополнительные иконки, если нужны */}
            {/* </div> */}

            {/* Информация о группе */}
            <div className="lesson-group">
              <span className="section-title">Практическое занятие, группа:</span> {lesson.group_name}
            </div>

            {/* Описание */}
            <div className="lesson-description">
              <span className="section-title">Описание:</span>
              {lesson.assignment_description || 'Нет описания'}
            </div>

            {/* Задание + кнопка выбора */}
            <div className="lesson-task">
              <span className="section-title">Задание:</span>
              <div className="task-row">
                {lesson.attachment_path ? (
                  <a href={lesson.attachment_path} target="_blank" rel="noopener noreferrer" className="task-link">
                    📎 {lesson.assignment_number}.pdf
                  </a>
                ) : (
                  <span className="no-file">Нет файла</span>
                )}
                <button className="file-select-btn">Выбрать файл</button>
              </div>
            </div>

            {/* Материалы (обучающие ресурсы) */}
            <div className="lesson-materials">
              <span className="section-title">Материалы (обучающие ресурсы):</span><br />
              <span className="lesson-materials-hint">Студенту будут доступны только отмеченные материалы. 
                Для загрузки материалов воспользуйтесь пунктом меню "Мои материалы".</span><br />
              <span className="no-info">Нет данных</span>
            </div>
          </div>
        ))
      )}
    </div>
  );
};

export default TeacherLessons;



// import React, { useState, useEffect } from 'react';
// import { Link } from 'react-router-dom';
// import api from '../api';

// const TeacherLessons = () => {
//   const [lessons, setLessons] = useState([]);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     fetchLessons();
//   }, []);

//   const fetchLessons = async () => {
//     try {
//       const response = await api.get('/lessons-detailed');
//       setLessons(response.data);
//     } catch (error) {
//       console.error('Ошибка загрузки занятий:', error);
//     } finally {
//       setLoading(false);
//     }
//   };

//   // Форматирование даты
//   const formatDate = (dateStr) => {
//     const d = new Date(dateStr);
//     return d.toLocaleDateString('ru-RU', { day: 'numeric', month: 'numeric', year: 'numeric' });
//   };

//   if (loading) return <div className="loading">Загрузка занятий...</div>;

//   return (
//     <div className="teacher-lessons">
//       {/* Заголовок и кнопка добавления */}
//       <div className="lessons-header">
//         {/* <h2>Занятия</h2> */}
//         <Link to="/teacher/add-lesson" className="button">+ Добавить занятие</Link>
//       </div>

//       {lessons.length === 0 ? (
//         <p className="empty-state">Нет доступных занятий</p>
//       ) : (
//         lessons.map(lesson => (
//           <div key={lesson.lesson_id} className="lesson-card">
//             {/* Верхняя строка: дата, иконки, группа, предмет */}
//             <div className="lesson-header">
//               <span className="lesson-date">{formatDate(lesson.lesson_date)}</span>
//               <div className="lesson-meta">
//                 <span className="meta-item">{lesson.subject_name}</span>
//                 <span className="meta-item">{lesson.group_name}</span>
//                 {/* Можно добавить курс, если есть данные */}
//               </div>
//             </div>

//             {/* Описание задания */}
//             <div className="lesson-description">
//               <div className="section-title">Описание:</div>
//               {lesson.assignment_description || 'Нет описания'}
//             </div>

//             {/* Блок задания (файл) */}
//             <div className="lesson-task">
//               <div className="section-title">Задание:</div>
//               {lesson.attachment_path ? (
//                 <a href={lesson.attachment_path} target="_blank" rel="noopener noreferrer" className="task-link">
//                   📎 {lesson.assignment_number}.pdf
//                 </a>
//               ) : (
//                 <span className="no-file">Нет файла</span>
//               )}
//             </div>

//             {/* Кнопка выбора файла и материалы */}
//             <div className="lesson-actions">
//               <button className="button-small file-select-btn">Выбрать файл</button>
//             </div>

//             {/* Заголовок материалов (без функционала) */}
//             <div className="lesson-actions">
//               <div className="section-title">Материалы (обучающие ресурсы):</div>
//               {/* Здесь можно ничего не выводить, если список не нужен */}
//                <span className="no-file">Нет информации</span>
//             </div> 
//           </div>
//         ))
//       )}
//     </div>
//   );
// };

// export default TeacherLessons;
