// src/pages/StudentLayout.jsx
import React, { useState, useEffect } from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import Header from '../components/Header';
import StudentLeftMenu from '../components/StudentLeftMenu';
import Footer from '../components/Footer';

const StudentLayout = () => {
  const location = useLocation();
  const [activeMenuItem, setActiveMenuItem] = useState('lessons');

  // Определяем активный пункт меню по пути (для подсветки)
  useEffect(() => {
    const path = location.pathname;
    if (path.includes('/student/lessons')) {
      setActiveMenuItem('lessons');
    } else {
      setActiveMenuItem('lessons'); // по умолчанию
    }
  }, [location]);

  const handleMenuItemSelect = (itemId) => {
    setActiveMenuItem(itemId);
    // Здесь можно добавить навигацию
  };

  return (
    <>
      <Header variant="personal" />
      <section id="ircode-body" className="ircode-body-second">
        <StudentLeftMenu activeItem={activeMenuItem} onSelect={handleMenuItemSelect} />
        <article className="text-content right-content">
          <div id="student-content">
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

export default StudentLayout;