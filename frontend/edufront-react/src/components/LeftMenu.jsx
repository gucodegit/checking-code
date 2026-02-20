// components/LeftMenu.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

const menuItems = [
  { id: 'materials', label: 'Мои материалы' },
  { id: 'classes', label: 'Занятия' },
  { id: 'tasks-answer', label: 'Задания для проверки' },
  { id: 'product', label: 'Продуктивные задания' },
  { id: 'product-history', label: 'История проверок продуктивных заданий' },
  { id: 'employments', label: 'Мои дисциплины' },
  { id: 'students', label: 'Студенты' },
  { id: 'students-dot', label: 'Студенты ДОТ' },
  { id: 'message-history', label: 'История сообщений' },
];

const LeftMenu = ({ activeItem, onSelect }) => {
  const navigate = useNavigate();

  const handleClick = (id) => {
    onSelect(id);  // сообщаем родителю об изменении активного пункта
    if (id === 'classes') navigate('/teacher/lessons');
    // ... другие переходы - аналогичные условия для других пунктов
  };

  return (
    <aside className="left-side">
      <div className="side-block">
        <div className="side-block-top">
          <h2>Меню</h2>
          <br className="close" />
        </div>
        <div className="side-block-body">
          <div id="teacherMenu">
            <ul>
              {menuItems.map((item) => (
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

export default LeftMenu;
