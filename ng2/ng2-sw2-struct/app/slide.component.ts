import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'slide-component',
  template: '<h1>{{ title }}</h1>',
  providers: []
})

export class SlideComponent  {
  title = 'slide container';
}