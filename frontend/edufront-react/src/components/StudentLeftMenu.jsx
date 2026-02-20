// src/components/StudentLeftMenu.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

// Пункты меню для студента (пока заглушки)
const menuItems = [
  { id: 'dashboard', label: 'Моя панель' },
  { id: 'lessons', label: 'Занятия' },
  { id: 'tasks', label: 'Мои решения' },
  { id: 'materials', label: 'Учебные материалы' },
  { id: 'messages', label: 'Сообщения' },
];

const StudentLeftMenu = ({ activeItem, onSelect }) => {
  const navigate = useNavigate();

  const handleClick = (id) => {
    onSelect(id);
    // Здесь можно добавить навигацию, когда появятся реальные страницы
    if (id === 'lessons') navigate('/student/lessons');
    // ... другие переходы - аналогичные условия для других пунктов
  };

  return (
    <aside className="left-side">
      <div className="side-block">
        <div className="side-block-top">
          <h2>Меню студента</h2>
          <br className="close" />
        </div>
        <div className="side-block-body">
          <div id="studentMenu">
            <ul>
              {menuItems.map(item => (
                <li
                  key={item.id}
                  data-action={item.id}
                  className={activeItem === item.id ? 'checked-item-menu' : ''}
                >
                  <span onClick={() => handleClick(item.id)}>{item.label}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </aside>
  );
};

export default StudentLeftMenu;
