import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'video-component',
  template: '<h1>{{ title }}</h1>',
  providers: []
})

export class VideoComponent  {
  title = 'video container';
}