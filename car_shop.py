# Ejercicio 9
import numpy as np
from generador import random_uniform_range

class Center:
    def __init__(self):
        self.queue = []
        self.time_left = -1
        self.job = None
        self.waiting_for_other_queue = 0
        self.finished_jobs = 0

    def work(self):
        if self.job:
            self.time_left -= 1
            self.job.wait()
    
    def assign_work(self, time):
        self.job = self.queue.pop(0)
        self.time_left = time
    
    def finish_job(self):
        work = self.job
        self.job = None
        self.time_left = -1
        self.finished_jobs += 1
        return work
    
    def is_empty(self):
        return self.time_left == -1
    
    def number_waiting(self):
        return len(self.queue)
    
    def wait_for_oher_queue(self):
        self.waiting_for_other_queue += 1
    
    def add_job_to_queue(self, job):
        self.queue.append(job)
    
    def total_jobs(self):
        return self.number_waiting() + int(self.is_empty())

class Job:
    def __init__(self):
        self.time = 0
    
    def wait(self):
        self.time += 1

def triangular_distribution():
    n = random_uniform_range(1, 5)
    if n <= 3:
        x = (n-1)/4
        return float_hours_to_minutes(x)
    else:
        x = (5-n)/4
        return float_hours_to_minutes(x)

def float_hours_to_minutes(hours):
    return int(round(hours*60))

def simulate_minute(center_a, center_b):
    finished_job = None
    
    if center_b.is_empty() and center_b.number_waiting() > 0:
        time = triangular_distribution()
        center_b.assign_work(time)
    
    if center_a.is_empty() and center_a.number_waiting() > 0:
        time = int(round(random_uniform_range(6,10)))
        center_a.assign_work(time)
    
    center_a.work()
    center_b.work()

    if (not center_a.is_empty()) and center_a.time_left == 0:
        if center_b.number_waiting() < 4:
            center_b.add_job_to_queue(center_a.finish_job())
        else:
            center_a.wait_for_oher_queue()
    
    if (not center_b.is_empty()) and center_b.time_left == 0:
        finished_job = center_b.finish_job()

    for job in center_a.queue:
        job.wait()
    for job in center_b.queue:
        if job:
            job.wait()
    
    total_jobs = center_a.total_jobs() + center_b.total_jobs()

    return total_jobs, finished_job

def simulate_hour(center_a, center_b, total_jobs_array, finished_jobs_array):
    new_cars = int(round(np.random.exponential(5)))

    for _ in range(new_cars):
        center_a.add_job_to_queue(Job())

    for _ in range(60):
        total_jobs, finished_job = simulate_minute(center_a, center_b)

        total_jobs_array.append(total_jobs)
        if finished_job:
            finished_jobs_array.append(finished_job.time)
    
    return total_jobs_array, finished_jobs_array

def simulation():
    center_a = Center()
    center_b = Center()
    total_jobs_array = []
    finished_jobs_array = []

    simulation_hours = 8
    for _ in range(simulation_hours):
        simulate_hour(center_a, center_b, total_jobs_array, finished_jobs_array)
    
    total_jobs = sum(total_jobs_array)/(simulation_hours*60) # Numero de trabajos esperados en cualquier momento
    a_waiting_time = center_a.waiting_for_other_queue/(simulation_hours*60) # Tiempo que centro a espero a centro b
    if (len(finished_jobs_array) > 0):
        finish_time = sum(finished_jobs_array)/len(finished_jobs_array) # Tiempo esperado de terminacion de un trabajo
    else:
        finish_time = 0

    return total_jobs, a_waiting_time, finish_time

if __name__ == "__main__":
    number_of_simulations = 1000
    print('nro_de_trabajos tiempo_a_esperando tiempo_de_terminacion')

    for i in range(number_of_simulations):
        total_jobs, a_waiting_time, finish_time = simulation()
        print(total_jobs, a_waiting_time, finish_time)