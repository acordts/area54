import { NgModule }       from '@angular/core';
import { BrowserModule }  from '@angular/platform-browser';
import { FormsModule }    from '@angular/forms';

import { AppComponent }         from './app.component';

import { AppRoutingModule }     from './app-routing.module';

import { WebcastService }         from './webcast.service';
import { UpcomingComponent }      from './upcoming.component';
import { OnDemandComponent }      from './ondemand.component';
import { WebcastDetailComponent } from './webcast-detail.component';

import { VideoComponent } from './video.component';
import { SlideComponent } from './slide.component';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule
  ],
  declarations: [
    AppComponent,
    UpcomingComponent,
    OnDemandComponent,
    WebcastDetailComponent,
    VideoComponent,
    SlideComponent
  ],
  providers: [
    WebcastService
   ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
