

def hanoi(n, source, target, auxiliary, step=1):
    if n == 1:
        print(f"Step {step}: Move disk 1 from {source} to {target}")
        return step
    step = hanoi(n-1, source, auxiliary, target, step)
    step += 1
    print(f"Step {step}: Move disk {n} from {source} to {target}")
    step = hanoi(n-1, auxiliary, target, source, step)
    step += 1
    return step

# 调用函数开始解决汉诺塔问题并计数
total_steps = hanoi(3, 'A', 'C', 'B')
print(f"Total moves needed: {total_steps}")