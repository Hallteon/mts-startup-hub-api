<h2>MTS-STARTUP-HUB API</h2>
<p><strong>MTS-STARTUP-HUB API - это API для мобильного приложения от МТС.</strong></p>

<p><strong>Список запросов API:</strong></p>

<ul>
    <li>api/startups/ - получить список стартапов при GET-запросе, создать новый стартап при 
    POST-запросе (передав данные).</li>
    <li>api/startups/&#60;int:pk&#62;/ - получить данные о стартапе при GET-запросе по pk стартапа, 
    обновить данные стартапа при POST-запросе, удалить стартап при DELETE-запросе.</li>
    <li>api/startups/program/&#60;int:pk&#62;/ - получить стартапы с определённой программой по pk 
    при GET-запросе.</li>
    <li>api/startups/stage/&#60;int:pk&#62;/ - получить стартапы с определённой стадией разработки 
    по pk при GET-запросе.</li>
    <li>api/programs/ - получить все программы при GET-запросе.</li>
    <li>api/stages/ - получить все стадии разработки при GET-запросе.</li>
    <li>api/programs/&#60;int:pk&#62;/ - получить конкретную программу по её pk при GET-запросе.</li>
    <li>api/stages/&#60;int:pk&#62;/ - получить конкретную стадию разработки при GET-запросе.</li>
    <li>api/events/ - получить всё мероприятия при GET-запросе, создать новое мероприятие при POST-запросе.</li>
    <li>api/events/&#60;int:pk&#62;/ - получить мероприятие по pk при GET-запросе, изменить мероприятие по pk 
    при POST-запросе, удалить мероприятие по pk при DELETE-запросе.</li>
    <li>api/auth/users/ - получить текущего пользователя при GET-запросе, создать нового пользователя при 
    POST-запросе.</li>
    <li>auth/token/login/ - залогиниться и получить токен пользователя при POST-запросе.</li>
</ul>

<p><strong>Поля модели пользователя:</strong></p>

<ul>
    <li>email - почта.</li>
    <li>firstname - имя.</li>
    <li>lastname - фамилия.</li>
    <li>password - пароль.</li>
</ul>

<p><strong>Поля модели стартапа:</strong></p>

<ul>
    <li>name - название стартапа.</li>
    <li>program - программа стартапа (pk).</li>
    <li>website - ссылка на сайт стартапа.</li>
    <li>stage - стадия разработки стартапа (pk).</li>
    <li>description - описание стартапа.</li>
    <li>presentation - ссылка на презентацию стартапа.</li>
</ul>

<p><strong>Поля модели мероприятия:</strong></p>

<ul>
    <li>name - название.</li>
    <li>platform - платформа (pk).</li>
    <li>description - описание.</li>
    <li>goals - цели.</li>
    <li>equipment - оборудование, которое предоставляет площадка.</li>
    <li>date - дата проведения мероприятия.</li>
</ul>

<p><strong>* При отправке запросов в API, нужно передавать в headers полу Authorization со 
значением - Token *Тут вставить токен пользователя без звёздочек*.</strong></p>