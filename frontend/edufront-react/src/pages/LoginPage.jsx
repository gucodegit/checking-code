import React, { useState } from 'react';
// import { useAuth } from '../context/AuthContext';
import { useAuth } from '../context/useAuth';
import { useNavigate } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';

const LoginPage = () => {
  const [username, setUsername] = useState('teacher');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username === 'teacher' && password === 'teacher') {
      login(username, password, 'teacher');
      navigate('/teacher');
    } else if (username === 'student' && password === 'student') {
      login(username, password, 'student');
      navigate('/student');
    } else if (username === 'student1' && password === 'student1') {
      login(username, password, 'student', { 
        groupName: 'ФКТ-224',
        fullName: 'Иван Петров'  // или загрузить с бэкенда 
      });
      navigate('/student');
    } else if (username === 'student2' && password === 'student2') {
      login(username, password, 'student', {
        groupName: 'ФКТ-224',
        fullName: 'Мария Смирнова'
      });
      navigate('/student');
    } else {
      alert('Неверные учетные данные');
    }
  };

  return (
    <>
      <section id="ircode-screen">
        <Header variant="main" />
        <section id="ircode-body">
          <div id="gu-dot-left-block" style={{ backgroundColor: '#fff', borderRadius: 15, fontSize: 17, color: 'black' }}>
            <div style={{ marginTop: 14 }}>
              Экранная лупа: Клавиша Windows <img style={{ verticalAlign: 'middle' }} width="40" src="/images/win.png" /> + Знак "плюс" (+)
            </div>
            <div style={{ paddingTop: 20 }}>
              Попасть в то место, где можно открыть экранную лупу, клавиатуру и диктора: Клавиша Windows {' '}
              <img width="40" style={{ verticalAlign: 'middle' }} src="/images/win.png" /> + U и выбрать
            </div>
          </div>
          <div id="gu-dot-right-block">
            <form onSubmit={handleSubmit}>
              <div className="input-type">
                <span>Логин или e-mail:</span>
                <input
                  className="textedit"
                  type="text"
                  id="username"
                  tabIndex="1"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />
                <br className="close" />
              </div>
              <div className="input-type">
                <span>Пароль:</span>
                <input
                  className="textedit"
                  type="password"
                  id="password"
                  tabIndex="2"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
                <br className="close" />
              </div>
              <div id="error-message"></div>
              <div id="login-aptitude"></div>
              <input
                id="login-button"
                type="submit"
                className="button"
                value="Вход"
              />
            </form>
          </div>
          <article className="text-content-main">
            <h1>Центр мониторинга качества образования в АНО&nbsp;ВО&nbsp;«Гуманитарный университет»</h1>
            <p>1 июля 2007 года в соответствии с решением Правления Гуманитарного университета по приказу ректора № 46/ОД от 27.06.2007 создан Центр мониторинга качества знаний Гуманитарного университета. 1 ноября 2009 года Центр мониторинга качества знаний преобразован в Центр компьютерных образовательных технологий. В соответствии с приказом № 101/ОД от 28 декабря 2018 Центр компьютерных образовательных технологий переименован в Центр мониторинга качества образования.</p>
            <p>Центр мониторинга качества образования решает следующие задачи:</p>
            <ul>
              <li>Разработка и сопровождение электронной информационно-образовательной среды Гуманитарного университета.</li>
              <li>Внедрение в учебный процесс компьютерных образовательных технологий.</li>
              <li>Мониторинг результатов обучения в университете с целью получения информации о характере и проблемах учебной работы каждого обучающегося.</li>
              <li>Организационное и технологическое обеспечение ректорского мониторинга качества знаний обучающихся университета.</li>
              <li>Организационное и технологическое обеспечение дополнительных профессиональных программ повышения квалификации научных и педагогических работников, сотрудников университета.</li>
              <li>Предоставление Интернет-услуг обучающимся, научным и педагогическим работникам, сотрудникам университета.</li>
              <li>Техническое сопровождение системы Антиплагиат.</li>
              <li>Организационное и технологическое обеспечение участия Гуманитарного университета в Федеральном интернет-экзамене в сфере профессионального образования (ФЭПО).</li>
            </ul>
          </article>
          <br className="close" />
        </section>
        {/* Добавляем отступ под футер */}
        <div id="footer-padding"></div>
      </section>
      <Footer />
    </>
  );
};

export default LoginPage;