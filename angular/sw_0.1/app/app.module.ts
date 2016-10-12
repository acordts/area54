import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import { VideoContainer } from './video.container/video.container'
import { SlidePreviewContainer } from './slide-preview.container/slide-preview.container'
import { SlideHistoryContainer } from './slide-history.container/slide-history.container'
import { AttachmentsContainer } from './attachments.container/attachments.container'
import { LinksContainer } from './links.container/links.container'
import { ChatContainer } from './chat.container/chat.container'

import { EmbedcodeService } from './embedcode.routing/embedcode.service'
import { EmbedcodeSurveyComponent } from './embedcode.routing/embedcode.survey.component'
import { EmbedcodeDetailComponent } from './embedcode.routing/embedcode.details.component'

import { routing } from './app.routing'

@NgModule({
  imports: [
    BrowserModule,
    routing
  ],
  declarations: [
	AppComponent,
	VideoContainer,
	SlidePreviewContainer,
	SlideHistoryContainer,
	AttachmentsContainer,
	LinksContainer,
	ChatContainer,
	EmbedcodeDetailComponent,
	EmbedcodeSurveyComponent
  ],
  providers: [
    EmbedcodeService
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
