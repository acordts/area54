import { Component } from '@angular/core';

@Component({
  moduleId: module.id,
  selector: 'portal',
  template: `
    <h1>{{title}}</h1>
    <p>header here</p>
    <nav>
      <a routerLink="/upcoming" routerLinkActive="active">Upcoming</a>
      <a routerLink="/ondemand" routerLinkActive="active">On-Demand</a>
      <a href="http://unfccc.int">UNFCCC Website</a>
    </nav>
    <router-outlet></router-outlet>
  `,
})

export class AppComponent {
  title = 'UNFCCC COP 22';
}
