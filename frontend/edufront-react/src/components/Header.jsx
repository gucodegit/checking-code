// components/Header.jsx
import React from 'react';
import { useAuth } from '../context/useAuth';
// import { useAuth } from '../context/AuthContext';

const Header = ({ variant = 'main' }) => {
  const { user, logout } = useAuth();

  if (variant === 'main') {
    return (
      <header>
        <div id="bg-header">
          <div id="header">
            <a id="gu-dot" href="/" rel="nofollow">
              <img src="/images/header-logo.png" alt="Гуманитарный университет" />
            </a>
            <nav>
              <ul>
                <li className="selected">Центр КОТ</li>
                <li><a href="/information">Информация</a></li>
                <li><a href="/contact">Контакты</a></li>
                <li><a href="/privacy">Политика КПДн</a></li>
              </ul>
              <br className="close" />
            </nav>
          </div>
        </div>
      </header>
    );
  }

  if (variant === 'personal') {
    return (
      <header className="header-second">
        <div id="bg-header">
          <div id="header">
            <a id="gu-dot" href="/" rel="nofollow">
              <img src="/images/header-logo.png" alt="Гуманитарный университет" />
            </a>
            <nav>
              <ul>
                <li className="selected">Личная страница</li>
                <li><a href="/portfolio">Портфолио</a></li>
                <li><a href="/privacy">Политика КПДн</a></li>
              </ul>
              <br className="close" />
            </nav>
            <div id="students-info">
              {/* Добро пожаловать, {user?.username || 'Пользователь'}<br /> */}
                Добро пожаловать, {user?.fullName || user?.username || 'Пользователь'}!<br />
              <div className="button" onClick={logout}>Выход</div>
            </div>
          </div>
        </div>
      </header>
    );
  }

  return null;
};

export default Header;
