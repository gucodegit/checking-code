// TeacherLayout.jsx
import React from 'react';
import { Outlet, useLocation, useNavigate } from 'react-router-dom';
import Header from '../components/Header';
import LeftMenu from '../components/LeftMenu';
import Footer from '../components/Footer';

const TeacherLayout = () => {
  const location = useLocation();
  const navigate = useNavigate();

  // Вычисляем активный пункт меню на основе текущего пути
  const getActiveMenuItem = () => {
    const path = location.pathname;
    if (path.includes('/teacher/lessons') || path.includes('/teacher/add-lesson')) {
      return 'classes';
    }
    // Добавьте другие условия для других разделов при необходимости
    return 'classes'; // по умолчанию
  };

  const activeMenuItem = getActiveMenuItem();

  const handleMenuItemSelect = (itemId) => {
    // Навигация на основе выбранного пункта меню
    switch (itemId) {
      case 'materials':
        navigate('/teacher/materials');
        break;
      case 'classes':
        navigate('/teacher/lessons');
        break;
      case 'tasks-answer':
        navigate('/teacher/tasks');
        break;
      // добавьте другие пункты по мере необходимости
      default:
        // Если маршрут не определён, можно ничего не делать
        break;
    }
  };

  return (
    <>
      <Header variant="personal" />
      <section id="ircode-body" className="ircode-body-second">
        <LeftMenu activeItem={activeMenuItem} onSelect={handleMenuItemSelect} />
        <article className="text-content right-content">
          <div id="teacher-lernen-content-polls"></div>
          <div id="teacher-content">
            <Outlet />
          </div>
        </article>
        <br className="close" />
      </section>
      <div id="footer-padding"></div>
      <Footer />
    </>
  );
};

export default TeacherLayout;
