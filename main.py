import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("요기추적")

# 베니부 체크 변수
check_var = tk.IntVar()

# 이전 인벤토리 상태
prev_gold = 0
prev_crystal = 0
prev_imposible = 0
prev_계귀 = 0
prev_교가 = 0

# 누적 획득량
gold_result = 0
crystal_result = 0
imposible_result = 0
total_계귀 = 0
total_교가 = 0

round_count = 0

def 계산(event=None):
    global prev_계귀, prev_교가, total_계귀, total_교가
    global prev_gold, prev_crystal, prev_imposible
    global gold_result, crystal_result, imposible_result
    global round_count

    try:
        now_gold = int(entry_gold.get())
        now_crystal = int(entry_crystal.get())
        now_계귀 = int(entry_계귀.get())
        now_교가 = int(entry_교가.get())

        now_imposible = now_계귀 + now_교가

        diff_gold = now_gold - prev_gold
        diff_crystal = now_crystal - prev_crystal
        diff_imposible = now_imposible - prev_imposible

        if check_var.get() == 1:
            diff_gold += 110000  # 베니부 보정

        gold_result += diff_gold
        crystal_result += diff_crystal
        imposible_result += diff_imposible
        total_계귀 += now_계귀 - prev_계귀
        total_교가 += now_교가 - prev_교가

        prev_gold = now_gold
        prev_crystal = now_crystal
        prev_imposible = now_imposible
        prev_계귀 = now_계귀
        prev_교가 = now_교가

        round_count +=1

        label_result.config(text=f"""
[이번 판 획득량]
골드: {diff_gold}
교가결정체: {diff_crystal}
계귀 잔흔: {now_계귀 - prev_계귀}
교가 잔흔: {now_교가 - prev_교가}

[총 누적 획득량]
골드: {gold_result}
교가결정체: {crystal_result}
계귀 잔흔: {total_계귀}
교가 잔흔: {total_교가}
판수 : {round_count}

[평균 수익]
골드 : {gold_result/round_count}
교가결정체 : {crystal_result/round_count}
계귀 잔흔: {total_계귀/round_count}
교가 잔흔: {total_교가/round_count}
판수 : {round_count/round_count}

        """.strip())


        entry_gold.delete(0, tk.END)
        entry_crystal.delete(0, tk.END)
        entry_계귀.delete(0, tk.END)
        entry_교가.delete(0, tk.END)
        entry_gold.focus()

        check_var.set(0)

    except ValueError:
        label_result.config(text="⚠ 숫자만 입력하세요!")


def 리셋():
    global prev_gold, prev_crystal, prev_imposible
    global gold_result, crystal_result, imposible_result

    if messagebox.askyesno("초기화 확인", "모든 데이터를 초기화할까요?"):
        prev_gold = prev_crystal = prev_imposible = 0
        gold_result = crystal_result = imposible_result = 0

        entry_gold.delete(0, tk.END)
        entry_crystal.delete(0, tk.END)
        entry_계귀.delete(0, tk.END)
        entry_교가.delete(0, tk.END)
        entry_gold.focus()
        check_var.set(0)

        label_result.config(text="[결과 초기화됨]")

# 입력 필드
labels = [
    "현재 골드:", 
    "현재 교가결정체:", 
    "현재 계귀 잔흔:", 
    "현재 교가 잔흔:"
    ]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=0, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

entry_gold, entry_crystal, entry_계귀, entry_교가 = entries

# 베니부 체크박스
tk.Checkbutton(root, text="베니부 사용 (자동 +11만 골드)", variable=check_var).grid(row=4, column=0, columnspan=2, pady=(5, 5))

# 버튼
tk.Button(root, text="계산", command=계산).grid(row=5, column=0, pady=10)
tk.Button(root, text="리셋", command=리셋, fg="red").grid(row=5, column=1, pady=10)

# 결과 라벨
label_result = tk.Label(root, text="[결과]", justify="left")
label_result.grid(row=6, column=0, columnspan=2)

# 엔터 키 바인딩
root.bind("<Return>", 계산)

# 시작 커서 위치
entry_gold.focus()

root.mainloop()
