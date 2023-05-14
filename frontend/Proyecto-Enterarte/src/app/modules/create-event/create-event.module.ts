import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { CreateEventRoutingModule } from './create-event-routing.module';
import { CreateEventComponent } from './pages/create-event/create-event.component';


@NgModule({
  declarations: [
    CreateEventComponent
  ],
  imports: [
    CommonModule,
    CreateEventRoutingModule,
    ReactiveFormsModule
  ]
})
export class CreateEventModule { }
